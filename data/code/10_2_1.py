class TemperatureComparator:
    def compare(self, temp1, temp2):
        if temp1 > temp2:
            print(f"{temp1} is greater than {temp2}")
        elif temp1 < temp2:
            print(f"{temp1} is less than {temp2}")
        else:
            print(f"{temp1} is equal to {temp2}")
if __name__ == '__main__':
    comparator = TemperatureComparator()
    comparator.compare(30, 25)
    comparator.compare(42, 42)
    comparator.compare(15, 50)