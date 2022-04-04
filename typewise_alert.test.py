import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(140, 50, 100) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.infer_breach(80, 50, 100) == 'NORMAL')
    
  def test_classify_temperature_breach_for_PASSIVE_COOLING(self):
     self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', -40)== 'TOO_LOW') 
     self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 35)== 'NORMAL') 
     self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', 50)== 'TOO_HIGH') 


if __name__ == '__main__':
  unittest.main()
