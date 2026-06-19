class TemperatureComparator:
    def compare(self, temp1, temp2):
        if temp1 > temp2:
            return f"{temp1} is higher than {temp2}"
        elif temp1 < temp2:
            return f"{temp1} is lower than {temp2}"
        else:
            return f"{temp1} and {temp2} are equal"

if __name__ == '__main__':
    comparator = TemperatureComparator()
    result = comparator.compare(30, 25)
    print(result)