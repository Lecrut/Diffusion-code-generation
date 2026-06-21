class TemperatureComparer:
    def __init__(self, temp1, temp2):
        self.temp1 = temp1
        self.temp2 = temp2

    def compare(self):
        difference = abs(self.temp1 - self.temp2)
        if self.temp1 > self.temp2:
            yield f"T1 is warmer by {difference} degrees"
        elif self.temp2 > self.temp1:
            yield f"T2 is warmer by {difference} degrees"
        else:
            yield "Both temperatures are equal"

if __name__ == '__main__':
    comparer1 = TemperatureComparer(30, 25)
    for result in comparer1.compare():
        print(result)

    comparer2 = TemperatureComparer(28, 35)
    for result in comparer2.compare():
        print(result)

    comparer3 = TemperatureComparer(20, 20)
    for result in comparer3.compare():
        print(result)

    comparer4 = TemperatureComparer(15, 22)
    for result in comparer4.compare():
        print(result)