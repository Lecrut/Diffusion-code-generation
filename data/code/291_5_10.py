def compare_measures(a_decimeters, a_centimeters, b_decimeters, b_centimeters):
    a_total = a_decimeters * 10 + a_centimeters
    b_total = b_decimeters * 10 + b_centimeters
    if a_total > b_total:
        return f"{a_decimeters} decimeters and {a_centimeters} centimeters"
    elif b_total > a_total:
        return f"{b_decimeters} decimeters and {b_centimeters} centimeters"
    else:
        return "Both measures are equal"

if __name__ == '__main__':
    print(compare_measures(2, 50, 3, 1))