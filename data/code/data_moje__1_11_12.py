class WeightManager:
    __STORAGE_KEY = '_internal_data'
    __INVALID_TYPE_ERROR = 'Value must be a numeric type'
    
    def __init__(self):
        self.__dict__[self.__STORAGE_KEY] = {}

    def __get_storage(self):
        return self.__dict__[self.__STORAGE_KEY]

    def __validate_weight(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(self.__INVALID_TYPE_ERROR)
        if isinstance(value, float) and value != value:
            raise ValueError('Weight cannot be NaN')

    def add_entry(self, identifier, value):
        self.__validate_weight(value)
        storage = self.__get_storage()
        storage[identifier] = float(value)
        return True

    def fetch_entry(self, identifier):
        storage = self.__get_storage()
        return storage.get(identifier)

    def modify_entry(self, identifier, value):
        self.__validate_weight(value)
        storage = self.__get_storage()
        if identifier in storage:
            storage[identifier] = float(value)
            return True
        return False

    def remove_entry(self, identifier):
        storage = self.__get_storage()
        if identifier in storage:
            del storage[identifier]
            return True
        return False

    def fetch_record(self, identifier):
        return self.fetch_entry(identifier)

    def get_record_count(self):
        return len(self.__get_storage())

    def get_all_records(self):
        return dict(self.__get_storage())

if __name__ == '__main__':
    mgr = WeightManager()
    mgr.add_entry('entry_alpha', 100.5)
    mgr.add_entry('entry_beta', 200.75)
    print(mgr.fetch_record('entry_alpha'))
    print(mgr.modify_entry('entry_alpha', 102.0))
    print(mgr.fetch_record('entry_alpha'))
    print(mgr.get_record_count())
    print(mgr.remove_entry('entry_beta'))
    print(mgr.get_all_records())