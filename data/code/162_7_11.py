class UserNameLengthMapper:
    def __init__(self):
        self.user_names = ["Alice", "Bob", "Charlie", "David"]

    def map_user_name_lengths(self):
        return {name: len(name) for name in self.user_names}

if __name__ == '__main__':
    mapper = UserNameLengthMapper()
    user_name_lengths = mapper.map_user_name_lengths()
    print(user_name_lengths)