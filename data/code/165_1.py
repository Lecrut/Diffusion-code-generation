class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def add_contact(self, name, phone):
        if not name or not phone:
            return False
        if not isinstance(name, str) or not isinstance(phone, str):
            return False
        self.name = name
        self.phone = phone
        return True
if __name__ == '__main__':
    contact1 = Contact("", "")
    print(f"Initial contact1: Name='{contact1.name}', Phone='{contact1.phone}'")
    success1 = contact1.add_contact("Alice", "123-456-7890")
    print(f"Attempt to add valid contact: {success1}")
    print(f"After adding valid contact: Name='{contact1.name}', Phone='{contact1.phone}'")
    contact2 = Contact("Bob", "987-654-3210")
    print(f"Initial contact2: Name='{contact2.name}', Phone='{contact2.phone}'")
    success2 = contact2.add_contact("", "555-1234")
    print(f"Attempt to add contact with empty name: {success2}")
    print(f"After adding invalid contact: Name='{contact2.name}', Phone='{contact2.phone}'")
    success3 = contact2.add_contact("Charlie", "")
    print(f"Attempt to add contact with empty phone: {success3}")
    print(f"After adding invalid contact: Name='{contact2.name}', Phone='{contact2.phone}'")
    contact3 = Contact("Diana", "111-222-3333")
    success4 = contact3.add_contact("Diana", "444-555-6666")
    print(f"Attempt to add valid contact: {success4}")
    print(f"After adding valid contact: Name='{contact3.name}', Phone='{contact3.phone}'")