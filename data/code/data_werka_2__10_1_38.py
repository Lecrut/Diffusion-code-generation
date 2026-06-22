class TemperatureComparator:

    def compare(self, temp1, temp2):
        if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
            raise ValueError('Both temperatures must be numbers.')
        if temp1 > temp2:
            return f'{temp1} is higher than {temp2}'
        elif temp1 < temp2:
            return f'{temp1} is lower than {temp2}'
        else:
            return f'{temp1} is equal to {temp2}'
if __name__ == '__main__':
    comparator = TemperatureComparator()
    try:
        print(comparator.compare(30, 25))
        print(comparator.compare(20, 20))
        print(comparator.compare(15, 22))
        print(comparator.compare('a', 22))
    except ValueError as e:
        print(e)