class FileHandler:
    DEFAULT_FILENAME = "sample_data.txt"
    
    @staticmethod
    def read_file(filename):
        try:
            with open(filename, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def process_and_print_first_last(self):
        items = self.read_file(FileHandler.DEFAULT_FILENAME)
        if items:
            first_item = items[0].strip()
            last_item = items[-1].strip()
            print(f"First item: {first_item}")
            print(f"Last item: {last_item}")

if __name__ == '__main__':
    with open(FileHandler.DEFAULT_FILENAME, 'w') as f:
        f.write("Apple\n")
    handler = FileHandler()
    handler.process_and_print_first_last()