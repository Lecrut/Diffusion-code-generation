check_mutual_exclusivity = lambda conditions: sum(conditions) == 1

if __name__ == '__main__':
    sample_conditions2 = (True, False, True)
    print(check_mutual_exclusivity(sample_conditions2))