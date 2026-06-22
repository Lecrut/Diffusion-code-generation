def compare_lengths(length1_decimeters, length1_centimeters, length2_decimeters, length2_centimeters):
    total_length1 = length1_decimeters * 10 + length1_centimeters
    total_length2 = length2_decimeters * 10 + length2_centimeters
    
    if total_length1 > total_length2:
        return f"{length1_decimeters} dm {length1_centimeters} cm"
    else:
        return f"{length2_decimeters} dm {length2_centimeters} cm"

if __name__ == '__main__':
    print(compare_lengths(5, 30, 4, 90))