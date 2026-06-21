class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current and current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.prepend(0)
    print("Linked List after append and prepend:", end=" ")
    current = linked_list.head
    while current:
        print(current.value, end=" ")
        current = current.next
    print()

    linked_list.delete(1)
    print("Linked List after delete:", end=" ")
    current = linked_list.head
    while current:
        print(current.value, end=" ")
        current = current.next
    print()

    search_result = linked_list.search(2)
    print(f"Search for 2: {search_result}")