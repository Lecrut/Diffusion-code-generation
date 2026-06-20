class Year:
    def __init__(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Year must be a non-negative integer.")
        self.value = value

    def difference_from(self, other_year):
        if not isinstance(other_year, Year):
            raise ValueError("Other year must be an instance of Year class.")
        return abs(self.value - other_year.value)

if __name__ == '__main__':
    year1 = Year(2023)
    year2 = Year(1990)
    print(year1.difference_from(year2))