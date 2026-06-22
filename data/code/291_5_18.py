class Measure:
    def __init__(self, decimeters, centimeters):
        self.decimeters = decimeters
        self.centimeters = centimeters

    def total_cm(self):
        return self.decimeters * 10 + self.centimeters

    def __str__(self):
        return f"{self.decimeters}dm {self.centimeters}cm"

def compare_measures(m1, m2):
    if m1.total_cm() > m2.total_cm():
        return m1
    else:
        return m2

if __name__ == '__main__':
    measure1 = Measure(3, 5)
    measure2 = Measure(4, 2)
    longer_measure = compare_measures(measure1, measure2)
    print(f"The longer measure is: {longer_measure}")