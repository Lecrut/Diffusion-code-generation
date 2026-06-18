import sys
def allocate_memory(size: int) -> list[int]:
    return [0] * size
if __name__ == '__main__':
    choice = 1
    if choice == 1:
        resource_size = 500_000
        data = allocate_memory(resource_size)
    elif choice == 2:
        resource_size = 5_000_000
        data = allocate_memory(resource_size)
    else:
        print("Invalid choice")
        sys.exit(1)
    memory_usage_mb = len(data) * (8 / (1024 ** 2)) if hasattr(sys, 'getsizeof') and isinstance(getattr(sys, 'getsizeof', lambda x: None)(data), int) else "Calculated"
    print(f"Allocated {len(data)} integers.")
    print(f"Estimated memory usage: ~{memory_usage_mb} MB")