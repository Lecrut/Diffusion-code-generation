class EmptyContainerError(Exception):
    def __init__(self, container_name):
        self.container_name = container_name
        super().__init__(f"Access denied: the provided {container_name} is empty")

def get_last_element(collection):
    length = len(collection)
    if length == 0:
        raise EmptyContainerError("list")
    return collection[length - 1]

if __name__ == '__main__':
    valid_list = [55, 66, 77, 88]
    last_item = get_last_element(valid_list)
    print(last_item)
    
    empty_list = []
    try:
        get_last_element(empty_list)
    except EmptyContainerError as exception:
        print(f"Error: {exception.container_name}")