division_map = {
    (10, 2): 5,
    (15.5, 3.0): 5.166666666666667
}

if __name__ == '__main__':
    result = division_map[(10, 2)]
    print(f"Result of 10 divided by 2: {result}")
    result2 = division_map[(15.5, 3.0)]
    print(f"Result of 15.5 divided by 3.0: {result2}")