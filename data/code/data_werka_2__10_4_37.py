class TemperatureComparator:
    WARMER_BY = " is warmer by {} degrees"
    EQUAL_TEMPS = "Both temperatures are equal"

    @staticmethod
    def compare(temp1, temp2):
        difference = abs(temp1 - temp2)
        if temp1 > temp2:
            yield f"T1{TemperatureComparator.WARMER_BY.format(difference)}"
        elif temp2 > temp1:
            yield f"T2{TemperatureComparator.WARMER_BY.format(difference)}"
        else:
            yield TemperatureComparator.EQUAL_TEMPS

if __name__ == '__main__':
    for result in TemperatureComparator.compare(30, 25):
        print(result)
    for result in TemperatureComparator.compare(20, 20):
        print(result)
    for result in TemperatureComparator.compare(15, 22):
        print(result)