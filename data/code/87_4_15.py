ELIGIBLE_PERMISSION = 'required_permission'

class Item:
    def __init__(self, active, permissions):
        self.active = active
        self.permissions = permissions
    
    @classmethod
    def is_eligible(cls, item):
        return item.active and ELIGIBLE_PERMISSION in item.permissions

if __name__ == '__main__':
    sample_item = Item(active=True, permissions=['required_permission', 'optional_permission'])
    print(Item.is_eligible(sample_item))