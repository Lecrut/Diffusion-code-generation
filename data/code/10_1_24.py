class TemperatureComparator:
    def compare(self, temp1, temp2):
        if temp1 > temp2:
            return f"{temp1} is higher than {temp2}."
        elif temp1 < temp2:
            return f"{temp1} is lower than {temp2}."
        else:
            return f"{temp1} is equal to {temp2}."

if __name__ == '__main__':
    comparator = TemperatureComparator()
    result1 = comparator.compare(30, 25)
    result2 = comparator.compare(20, 20)
    result3 = comparator.compare(15, 22)
    
    print(result1)
    print(result2)
    print(result3)