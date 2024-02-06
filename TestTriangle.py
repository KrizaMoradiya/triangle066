# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
@author: jrr
@author: rk
"""
import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):

    def testEquilateralTriangle(self):
        self.assertEqual(classifyTriangle(3, 3, 3), 'Equilateral', '3,3,3 should be equilateral')

    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(3, 4, 3), 'Isosceles', '3,4,3 should be isosceles')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(5,6,7), 'Scalene', '5,6,7 should be scalene')

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a right-angled triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a right-angled triangle')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1, 1, 2), 'NotATriangle', '1,1,2 is not a triangle')

    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(201, 100, 150), 'InvalidInput', '201,100,150 is invalid input')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
