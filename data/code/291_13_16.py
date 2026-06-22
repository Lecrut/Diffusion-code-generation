def compare_measurements(km: float, miles: float) -> str:
    conversion_factor = 0.621371
    if km * conversion_factor > miles:
        return f"{km:.2f} km"
    else:
        return f"{miles:.2f} mi"

if __name__ == '__main__':
    print(compare_measurements(10, 15))
    print(compare_measurements(5.5, 3.4))