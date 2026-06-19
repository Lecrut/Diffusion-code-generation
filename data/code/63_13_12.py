class SafeSequenceAccess:
    def __init__(self, sequence):
        self.sequence = sequence

    def get_first_element(self):
        return self.sequence[0] if self.sequence else None

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_tuple = (4, 5, 6)
    empty_list = []
    empty_tuple = ()
    
    safe_access_list = SafeSequenceAccess(sample_list)
    safe_access_tuple = SafeSequenceAccess(sample_tuple)
    safe_access_empty_list = SafeSequenceAccess(empty_list)
    safe_access_empty_tuple = SafeSequenceAccess(empty_tuple)
    
    print(safe_access_list.get_first_element())
    print(safe_access_tuple.get_first_element())
    print(safe_access_empty_list.get_first_element())
    print(safe_access_empty_tuple.get_first_element())