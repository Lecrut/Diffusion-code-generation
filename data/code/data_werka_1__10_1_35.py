class TemperatureComparator:
    def compare(self, temp1, temp2):
        if temp1 > temp2:
            return f"{temp1} is higher than {temp2}"
        elif temp1 < temp2:
            return f"{temp1} is lower than {temp2}"
        else:
            return f"{temp1} is equal to {temp2}"

if __name__ == '__main__':
    comparator = TemperatureComparator()
    print(comparator.compare(25, 30))
    print(comparator.compare(40, 20))
    print(comparator.compare(35, 35))