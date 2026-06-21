class TemperatureComparator:
    def compare(self, temp1, temp2):
        if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
            raise ValueError("Both temperatures must be numbers.")
        
        difference = temp1 - temp2
        if difference > 0:
            return f"{temp1} is higher than {temp2}"
        elif difference < 0:
            return f"{temp1} is lower than {temp2}"
        else:
            return f"{temp1} is equal to {temp2}"

if __name__ == '__main__':
    comparator = TemperatureComparator()
    print(comparator.compare(35, 28))
    print(comparator.compare(40, 40))
    print(comparator.compare(22, 27))