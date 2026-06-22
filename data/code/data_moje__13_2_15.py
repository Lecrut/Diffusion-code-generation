class TupleAccessError(Exception):
    def __init__(self, index, length):
        self.index = index
        self.length = length
        message = f"Cannot access index {index}: tuple length is {length}"
        super().__init__(message)

def retrieve_item(data_tuple, position):
    length = len(data_tuple)
    if not isinstance(position, int):
        raise TypeError("Position must be an integer")
    if position >= length or position < -length:
        raise TupleAccessError(position, length)
    return data_tuple[position]

if __name__ == '__main__':
    inventory = ('hammer', 'wrench', 'screwdriver', 'pliers', 'saw')
    item = retrieve_item(inventory, 3)
    print(item)
    try:
        invalid_item = retrieve_item(inventory, 8)
        print(invalid_item)
    except TupleAccessError as error:
        print(f"Error caught: {error}")