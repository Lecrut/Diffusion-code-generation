def check_mutual_exclusivity(conditions: tuple) -> bool:
    return sum(map(int, conditions)) == 1

if __name__ == '__main__':
    sample_values = (True, False, True)
    print(check_mutual_exclusivity(sample_values))