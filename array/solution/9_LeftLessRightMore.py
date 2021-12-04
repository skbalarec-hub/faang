# We have an array, we have to find an element before which all elements are less than it, and after which all are greater than it.
# Finally, return the index of the element, if there is no such element, then return -1:
# Time complexity O(n) and Space Complexity O(n)

import unittest
import sys


def findElement(array, n):

       # Write your code here
    left = 10 * [0]

    for i in range(1, n):
        left[i] = max(left[i-1], array[i-1])

    right = sys.maxsize
    for i in range(n-1, 0, -1):
        if (left[i] < array[i] and right > array[i]):
            return i
        right = min(right, array[i])

    return -1

# ok for all test cases required

class Test(unittest.TestCase):
    def test_findElement1(self):
        actual = findElement([5, 1, 4, 3, 6, 8, 10, 7, 9], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_findElement2(self):
        actual = findElement([6, 2, 5, 4, 7, 9, 11, 8, 10], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_findElement3(self):
        actual = findElement([5, 1, 4, 4], 4)
        expected = -1
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
