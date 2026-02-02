# Cart functionality

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        if product in self.items:
            self.items.remove(product)

    def get_items(self):
        return self.items
