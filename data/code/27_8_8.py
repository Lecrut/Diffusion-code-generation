import hashlib

def is_sum_different(list1: list[int], list2: list[int]) -> bool:
    """Returns True if sum of elements in list1 differs from sum of elements in list2."""
    return sum(list1) != sum(list2)

if __name__ == '__main__':
    a = [1, 5, -3]
    b = [4, 6]
    
    # Using the function to check if sums are different
    result = is_sum_different(a, b)
    
    print("List A:", a)
    print("Sum of List A:", sum(a))
    print("\nList B:", b)
    print("Sum of List B:", sum(b))
    print(f"\nAre sums different? {result}")

    # Additional test case for demonstration with larger lists (simulated efficiency by hash approach conceptually, though standard sum is O(n+M) which is optimal without hashing overhead unless precomputed hashes were stored).