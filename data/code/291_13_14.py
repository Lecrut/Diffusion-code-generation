def compare_measurements(km, miles):
    conversion_factor = 0.621371
    if km > miles / conversion_factor:
        return f"{km:.2f} km"
    else:
        return f"{miles * conversion_factor:.2f} km"

if __name__ == '__main__':
    print(compare_measurements(10, 6.21))
    print(compare_measurements(5, 8))