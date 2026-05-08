import unittest
def decision_maker(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"
class TestDecisionMaker(unittest.TestCase):
    def test_grade_a(self):
        self.assertEqual(decision_maker(95), "A")
        self.assertEqual(decision_maker(100), "A")
    def test_grade_b(self):
        self.assertEqual(decision_maker(85), "B")
        self.assertEqual(decision_maker(80), "B")
    def test_grade_c(self):
        self.assertEqual(decision_maker(75), "C")
        self.assertEqual(decision_maker(70), "C")
    def test_grade_f(self):
        self.assertEqual(decision_maker(69), "F")
        self.assertEqual(decision_maker(0), "F")
    def test_boundary_conditions(self):
        self.assertEqual(decision_maker(90), "A")
        self.assertEqual(decision_maker(89), "B")
        self.assertEqual(decision_maker(79), "C")
        self.assertEqual(decision_maker(69), "F")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)