store_ages = {
    "Store A": 25,
    "Store B": 30,
    "Store C": 45,
    "Store D": 20,
    "Store E": 35
}

class StoreAgeManager:
    STORE_AGE_LIMIT = 18
    
    @staticmethod
    def validate_store_name(store_name):
        if not isinstance(store_name, str) or store_name.strip() == "":
            raise ValueError("Invalid store name")
    
    @staticmethod
    def validate_age(age):
        if not isinstance(age, int) or age < StoreAgeManager.STORE_AGE_LIMIT:
            raise ValueError(f"Invalid age. Age must be an integer greater than {StoreAgeManager.STORE_AGE_LIMIT}.")
    
    @classmethod
    def add_store_age(cls, store_name, age):
        cls.validate_store_name(store_name)
        cls.validate_age(age)
        store_ages[store_name] = age
    
    @classmethod
    def get_store_age(cls, store_name):
        cls.validate_store_name(store_name)
        return store_ages.get(store_name, None)

if __name__ == '__main__':
    StoreAgeManager.add_store_age("Store F", 22)
    print(f"Updated store ages: {store_ages}")
    try:
        print(f"Age of Store A: {StoreAgeManager.get_store_age('Store A')}")
    except ValueError as e:
        print(e)