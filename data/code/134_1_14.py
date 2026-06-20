def check_mutual_exclusivity(bitmask):
    return bitmask & bitmask - 1 == 0
if __name__ == '__main__':
    print(check_mutual_exclusivity(1))
    print(check_mutual_exclusivity(2))
    print(check_mutual_exclusivity(3))
    print(check_mutual_exclusivity(4))
    print(check_mutual_exclusivity(0))