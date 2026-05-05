def main():
    my_list = [10, 20, 30, 40, 50]
    print("Original List:", my_list)
    print("\nAccessing elements using positive indices:")
    print("Element at index 0:", my_list[0])
    print("Element at index 2:", my_list[2])
    print("Element at the last index (index -1):", my_list[-1])
    print("Element at the second to last index (index -2):", my_list[-2])
    print("\nAccessing elements using negative indices:")
    print("Element at index -1:", my_list[-1])
    print("Element at index -3:", my_list[-3])
    print("\nSlicing:")
    print("Slice from index 1 to 3 (exclusive):", my_list[1:4])
    print("Slice from the beginning to index 3:", my_list[:3])
    print("Slice from index 2 to the end:", my_list[2:])
    print("Slice from the beginning to the end:", my_list[:])
if __name__ == '__main__':
    main()