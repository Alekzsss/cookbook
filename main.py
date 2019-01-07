from itertools import count

class Receipt(object):
    """Блюдо - название должно быть уникально"""

    _ids = count(1)

    def __init__(self, name, ingredients, text):
        self.name = name
        self.ingredients = ingredients
        self.text = text
        self.id = next(self._ids)

    def view(self):
        print('Рецепт #{}'.format(self.id))
        print('{}'.format(self.name))
        print('Ингредиенты: {}'.format(self.ingredients))
        print('{}'.format(self.text+'\n'))

def main():
    test_receipt_name = 'Омлет'
    test_receipt_name_2 = 'Омлет 2'
    test_ingredients = ["3 яйца", "столовая ложка молока", "соль", "перец", "масло сливочное"]
    test_receipt_text = """
Вылейте яйца в тарелку, добавьте столовую ложку
молока, соль и перец, взбейте.
Нагрейте на среднем огне сковороду, 
положите на горячую сковороду масло, вылейте на сковороду яйца.
Когда омлет поджарится с одной стороны, 
переверните его с помощью лопатки.
При желании, добавьте в омлет тертый сыр, 
приправы и другие добавки(грибы, лук, сладкий, перец, спаржа, др.)."""
    test_receipt = Receipt(test_receipt_name, test_ingredients, test_receipt_text)
    test_receipt_2 = Receipt(test_receipt_name_2, test_ingredients, test_receipt_text)
    test_receipt.view()
    test_receipt_2.view()

if __name__ == '__main__':
    main()
