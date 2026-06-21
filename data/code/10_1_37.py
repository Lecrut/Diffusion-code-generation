class TemperatureComparator:
    def compare(self, temp1, temp2):
        comparison_map = {
            1: f"{temp1} is higher than {temp2}",
            -1: f"{temp1} is lower than {temp2}",
            0: f"{temp1} is equal to {temp2}"
        }
        
        if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
            raise ValueError("Both temperatures must be numbers.")
        
        result_key = (temp1 > temp2) - (temp1 < temp2)
        return comparison_map[result_key]

if __name__ == '__main__':
    comparator = TemperatureComparator()
    print(comparator.compare(30, 25))
    print(comparator.compare(20, 20))
    print(comparator.compare(15, 22))