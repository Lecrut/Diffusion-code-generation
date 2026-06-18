import sys
def allocate_memory(size: int) -> bytes:
    return b'\x00' * size
if __name__ == '__main__':
    choice = 1 if len(sys.argv) > 1 else None
    try:
        user_choice = int(choice or "2")
        if user_choice == 1:
            size = 4096
            data = allocate_memory(size)
        elif user_choice == 2:
            size = 8388608
            data = allocate_memory(size)
        else:
            raise ValueError("Invalid choice")
    except Exception as e:
        sys.exit(1)