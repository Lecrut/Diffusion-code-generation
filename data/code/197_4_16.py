class ChecklistMapper:
    MEMBERSHIP_STATUS = {
        'item1': 'Member',
        'item2': 'Non-Member',
        'item3': 'Pending'
    }

    @staticmethod
    def map_checklist_items(checklist: set) -> dict:
        return {item: ChecklistMapper.MEMBERSHIP_STATUS.get(item, 'Unknown') for item in checklist}

if __name__ == '__main__':
    sample_checklist = {'item1', 'item4'}
    mapper = ChecklistMapper()
    result = mapper.map_checklist_items(sample_checklist)
    print(result)