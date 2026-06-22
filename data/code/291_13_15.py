def compare_lengths(km, miles):
    conversion_factor = 0.621371
    if km * conversion_factor > miles:
        return f"{km:.2f} km"
    else:
        return f"{miles:.2f} mi"

if __name__ == '__main__':
    print(compare_lengths(5, 8))