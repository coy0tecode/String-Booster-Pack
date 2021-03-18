# -*- coding: utf-8 -*-


import unittest
from string_booster import string_booster as sb



class Testcctrans(unittest.TestCase):
    
    
    def test_1(self):
        self.assertEqual(sb.cctrans(1234567890123456), '************3456',
                         'Output should be - ************3456')
        
    def test_2(self):
        self.assertEqual(sb.cctrans('  1234_5678-9012 3456  '), '************3456',
                         'Output should be - ************3456')
        
    def test_3(self):
        self.assertEqual(sb.cctrans(123456789), '*****6789',
                         'Output should be - *****6789')
        
        
class Testsstrans(unittest.TestCase):
    
    
    def test_1(self):
        self.assertEqual(sb.sstrans(123456789), '*****6789', 
                         'Output should be - *****6789')
    
    def test_2(self):
        self.assertEqual(sb.sstrans('  123 _45-6789- '), '*****6789',
                         'Output should be - *****6789')
        
    def test_3(self):
        self.assertEqual(sb.sstrans(123456), '**3456',
                         'Output should be - **3456')
        
        
# passgen has already been tested


class Testbtitle(unittest.TestCase):
    
    
    def test_1(self):
        self.assertEqual(sb.btitle('python And THE 14 squids', ['and', 'the']),
                         'Python and the 14 Squids',
                         'Output should be - Python and the 14 Squids')
        
    def test_2(self):
        self.assertEqual(sb.btitle('PYTHON in tHe Year 2088: AN expose', ['in', 'the', 'an']),
                         'Python in the Year 2088: an Expose',
                         'Output should be - Python in the Year 2088: an Expose')
        
        
class Testemailfinder(unittest.TestCase):
    
    
    def test_1(self):
        self.assertEqual(sb.emailfinder('My email is: testperson@gmail.com'),
                         ['testperson@gmail.com'],
                         'Output did not match expected')
        
        
class Testcensor(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(sb.censor('This is a Test', ['test'], '*'),
                         'This is a ****',
                         'Output should be - This is a ****')
        
        
class Testredactor(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(sb.redactor('This is a test', ['test']), 
                         'This is a [redacted]', 
                         'Output should be - This is a [redacted]')
        
        
class Testasciifinder(unittest.TestCase):

    def test_1(self):
        self.assertEquals(sb.asciifinder('Test'),
                          {'T' : 84, 'e' : 101, 's' : 115, 't' : 116},
                          'Output did not match expected dictionary')
        
        
class Testasciicipher(unittest.TestCase):
    
    def test_1(self):
        self.assertEquals(sb.asciicipher('Test', 2), 'Uguz', 
                          'Output should be - Uguz')
        
        
class Testasciidecrypter(unittest.TestCase):
    
    def test_1(self):
        self.assertEquals(sb.asciidecrypter('Uguz'), 'Test',
                          'Output should be - Test')
        
        

        
        
        
        
        
        
        
        
        