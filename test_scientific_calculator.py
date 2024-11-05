import unittest
import math
from scientific_calculator import sin_function, cos_function, tan_function, log_function, sqrt_function, exp_function

class test_scientific_calculator(unittest.TestCase):
    def test_sinPositive(self):
        sin_positiveValue = sin_function(90)
        self.assertAlmostEqual(sin_positiveValue, 1)
    def test_sinNegative(self):
        sin_negativeValue = sin_function(-90)
        self.assertAlmostEqual(sin_negativeValue, -1)
    def test_sinZero(self):
        sin_zeroValue = sin_function(0)
        self.assertAlmostEqual(sin_zeroValue, 0)
    def test_sinString(self):
        with self.assertRaises(TypeError):
            sin_function("some Text")
    
    def test_cosPositive(self):
        cos_positiveValue = cos_function(90)
        self.assertAlmostEqual(cos_positiveValue, 0)
    def test_cosNegative(self):
        cos_negativeValue = cos_function(-90)
        self.assertAlmostEqual(cos_negativeValue, 0)
    def test_cosZero(self):
        cos_zeroValue = cos_function(0)
        self.assertAlmostEqual(cos_zeroValue, 1)
    def test_cosString(self):
        with self.assertRaises(TypeError):
            cos_function("some Text")
    
    def test_tanPositive(self):
        tan_positiveValue = tan_function(45)
        self.assertAlmostEqual(tan_positiveValue, 1)
    def test_tanNegative(self):
        tan_negativeValue = tan_function(-45)
        self.assertAlmostEqual(tan_negativeValue, -1)
    def test_tanZero(self):
        tan_zeroValue = tan_function(0)
        self.assertAlmostEqual(tan_zeroValue, 0)
    def test_tanString(self):
        with self.assertRaises(TypeError):
            tan_function("some Text")
    
    def test_sqrtPositive(self):
        sqrt_positiveValue = sqrt_function(4)
        self.assertAlmostEqual(sqrt_positiveValue, 2)
    def test_sqrtNegative(self):
        with self.assertRaises(ValueError):
            sqrt_function(-45)
    def test_sqrtZero(self):
        sqrt_zeroValue = sqrt_function(0)
        self.assertAlmostEqual(sqrt_zeroValue, 0)
    def test_sqrtString(self):
        with self.assertRaises(TypeError):
            sqrt_function("some Text")
    
    
    def test_logPositive(self):
        log_positiveValue = log_function(2)
        self.assertAlmostEqual(log_positiveValue, 0.6931471805599453)
    def test_logNegative(self):
        with self.assertRaises(ValueError):
            log_function(-45)
    def test_logZero(self):
        with self.assertRaises(ValueError):
            log_function(0)
    def test_logString(self):
        with self.assertRaises(TypeError):
            log_function("some Text")

    def test_expPositive(self):
        exp_positiveValue = exp_function(5)
        self.assertAlmostEqual(exp_positiveValue, 148.4131591025766)
    def test_expNegative(self):
        exp_negativeValue = exp_function(-1)
        self.assertAlmostEqual(exp_negativeValue, 0.36787944117144233)
    def test_expZero(self):
        exp_zeroValue = exp_function(0)
        self.assertAlmostEqual(exp_zeroValue, 1.0)
    def test_expString(self):
        with self.assertRaises(TypeError):
            exp_function("some Text")
    
   

if __name__ == '__main__':
    unittest.main()

