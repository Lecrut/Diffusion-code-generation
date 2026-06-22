def compare_measurements(km, miles):
    conversion_factor = 0.621371
    if km * conversion_factor > miles:
        return f"{km:.2f} kilometers"
    else:
        return f"{miles:.2f} miles"

if __name__ == '__main__':
    print(compare_measurements(10, 6))
    print(compare_measurements(5, 8.04672))