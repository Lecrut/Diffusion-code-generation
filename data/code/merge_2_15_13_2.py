import sys
def sort_integers(data):
    return sorted(data)
def sort_floats(data):
    if len(sys.argv) > 1:
        is_reverse = sys.argv[1].lower() == 'reverse'
    else:
        is_reverse = False
    return sorted(data, reverse=is_reverse)
def main():
    integer_dataset = [45023, 8765, -9871, 12345, -567]
    float_dataset = [3.14159, 2.71828, 1.41421, 0.57721, 2.30258]
    sorted_integers = sort_integers(integer_dataset)
    sorted_floats_asc = sort_floats(float_dataset)
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'reverse':
        sorted_floats_desc = sort_floats(float_dataset, is_reverse=True)
    else:
        sorted_floats_desc = list(reversed(sorted_floats_asc))
    print("Sorted Integers:")
    print(sorted_integers)
    print("\nSorted Floats (Ascending):")
    print(sorted_floats_asc)
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'reverse':
        print("\nSorted Floats (Descending):")
        print(sorted_floats_desc)
if __name__ == '__main__':
    main()