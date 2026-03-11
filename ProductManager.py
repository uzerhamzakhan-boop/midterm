class ProductManager:

    def __init__(self):
        self.products = []

    def addProduct(self, name, price):
        product = {"name": name, "price": price}
        self.products.append(product)

    def listProducts(self):
        return self.products
