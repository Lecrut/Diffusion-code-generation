class Measure:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def to_cm(self):
        if self.unit == 'cm':
            return self.value
        elif self.unit == 'm':
            return self.value * 100
        else:
            raise ValueError("Unsupported unit")

    def compare_to(self, other):
        length1_cm = self.to_cm()
        length2_cm = other.to_cm()
        if length1_cm < length2_cm:
            return self
        elif length2_cm < length1_cm:
            return other
        else:
            return None

if __name__ == '__main__':
    m1 = Measure(50, 'cm')
    m2 = Measure(3, 'm')
    shorter_measure = m1.compare_to(m2)
    if shorter_measure:
        print(f"The shorter measure is {shorter_measure.value} {shorter_measure.unit}")
    else:
        print("Both measures are equal")