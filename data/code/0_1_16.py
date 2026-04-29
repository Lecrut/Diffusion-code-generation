class DynamicListManager:
    def __init__(self):
        self.data = []

    def add_element(self, value: int) -> None:
        self.data.append(value)

    def get_list(self) -> list:
        return self.data

def process_list_data(manager: DynamicListManager, initial_value: int, additions: list[int]) -> tuple[list[int], int]:
    result = manager.get_list()
    total = len(result)
    for value in additions:
        manager.add_element(value)
    final_count = len(result)
    return result, final_count

if __name__ == '__main__':
    manager = DynamicListManager()
    initial_value = 10
    additions = [5, 20, 15]

    result, count = process_list_data(manager, initial_value, additions)

    print(result)
    print(count)