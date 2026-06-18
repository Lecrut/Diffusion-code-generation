import sys
class MemoryManager:
    def __init__(self):
        self.buffer_size = 0
        self.data_store = []
    def allocate(self, size_choice):
        if size_choice == 1:
            self.buffer_size = 64 * 1024
            return bytearray(self.buffer_size)
        elif size_choice == 2:
            self.buffer_size = 512 * 1024
            return bytearray(self.buffer_size)
        else:
            raise ValueError("Invalid choice")
    def process_data(self, data):
        if len(data) > self.buffer_size // 8:
            chunked_results = []
            for i in range(0, len(data), self.buffer_size // 16):
                chunk = data[i:i + (self.buffer_size // 16)]
                processed_chunk = bytearray(chunk * 2)
                chunked_results.append(processed_chunk)
            return b''.join(chunked_results)
        else:
            return data
def main():
    choice_map = {
        "small": 1,
        "medium": 2,
        "large": None
    }
    sample_choice = list(choice_map.keys())[0] if not sys.stdin.isatty() else input("Enter resource allocation strategy (small/medium/large): ").strip().lower()
    try:
        size_idx = choice_map.get(sample_choice) or 1
    except Exception as e:
        print(f"Error selecting strategy: {e}")
        return
    manager = MemoryManager()
    allocated_memory = manager.allocate(size_idx)
    sample_data = bytearray(range(0, min(len(allocated_memory), 50)))
    processed_output = manager.process_data(sample_data)
    print(f"Allocated memory size: {len(allocated_memory)} bytes")
    if len(processed_output) > 10:
        print("Processing complete (output truncated)")
    else:
        print(processed_output.hex())
if __name__ == '__main__':
    main()