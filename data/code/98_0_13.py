class BooleanConditionTester:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def evaluate(self):
        if self.x > 10 and self.y < 5:
            return "High X and Low Y"
        elif self.z == 0:
            return "Zero Z"
        elif self.x == self.y:
            return "Equal X and Y"
        else:
            return "Default Case"

    def get_status_summary(self):
        if self.x > 10:
            x_status = "High"
        else:
            x_status = "Low"
        
        if self.y < 5:
            y_status = "Low"
        else:
            y_status = "High"
            
        return f"X: {x_status}, Y: {y_status}, Z: {self.z}"

if __name__ == '__main__':
    tester = BooleanConditionTester(15, 3, 5)
    print(tester.evaluate())
    print(tester.get_status_summary())
    
    tester2 = BooleanConditionTester(5, 12, 0)
    print(tester2.evaluate())
    print(tester2.get_status_summary())