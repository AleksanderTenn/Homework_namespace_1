

def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
#inner_function() # выдает ошибку, так как inner_function() находится в локалльной
#области видимости фунции test_function()

test_function()