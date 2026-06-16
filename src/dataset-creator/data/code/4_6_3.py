import sys
def allocate_memory_resource(choice: int) -> bytes:
    if choice == 1:
        return b'\x00' * (2 ** 8)
    elif choice == 2:
        return bytearray(4 * 1024).tobytes()
    else:
        raise ValueError("Invalid resource allocation choice.")
if __name__ == '__main__':
    sample_choice = 1
    try:
        memory_block = allocate_memory_resource(sample_choice)
        if len(memory_block) > 65536:
            print(f"Allocated {len(memory_block)} bytes for large resource.")
        else:
            print(f"Small allocation of {len(memory_block)} bytes completed successfully.")
    except ValueError as e:
        sys.exit(1)