import json
from typing import List, Dict, Any

def load_data(filename : str) -> List[Dict[str ,Any]] :
  """
  Đọc dữ liệu từ file JSON và in danh sách sản phẩm
  Args:
    filename (Str) : Đường dẫn tới file JSON
  Return:
    products (List[Dict[Str, Any]]) : Danh sách sản phẩm
  """

  with open(filename, 'r') as file:
    products = json.load(file)
  print("Danh sách sản phẩm ")
  for product in products :
    print(product)
  return products
if __name__ == '__main__':
    filename = "products.json"
    load_data(filename)

def filter_low_stock(products: List[Dict[str ,Any]]) -> List[Dict[str ,Any]]:
  """
  Lọc sản phẩm có số lượng dưới 10
  Args:
    products (List[Dict[str ,Any]) : Danh sách sản phẩm
  Return:
    low_stock_products (List[Dict[str, Any]) : Danh sách sản phẩm có số lượng dưới 10
  """
  low_stock_products = [product for product in products if product['inventory']['quantity'] < 10 ]
  return low_stock_products
if __name__ == '__main__':
    filename = "products.json"
    products = load_data(filename)

    low_stock_products = filter_low_stock(products)
    print("\nDanh sách sản phẩm có số lượng dưới 10 :")
    for product in low_stock_products:
        print(product)



def update_quantity(products: List[Dict[str, Any]], product_id: int, new_quantity: int ) -> List[Dict[str, Any]]:

    """
    Cập nhật số lượng sản phẩm theo ID
    Args:
      products (List[Dict[str, Any) : Danh sách sản phẩm
      product_id (int) : ID sản phẩm cần cập nhật
      new_quantity (int) : Số lượng mới
    Return:
      List(Dict[str, Any]) : Danh sách sản phẩm sau khi cập nhật
    """
    for product in products :
      if product["id"] == product_id :
        product["inventory"]["quantity"] = new_quantity
        break
    return products
if __name__ == '__main__':
    filename = "products.json"
    products = load_data(filename)

    product_id = 4
    new_quantity = 20
    products = update_quantity(products, product_id, new_quantity)

    print(f" Đã cập nhật số lượng của sản phẩm có ID {product_id} thành {new_quantity} ")



def save_data(filename: str, products: List[Dict[str, Any]]) -> None:
    """
    Lưu dữ liệu vào file JSON
    Args:
      filename (str): Đường dẫn file JSON
      products (List[Dict[str, Any]]) : Danh sách sản phẩm
    Return:
      None
    """
    with open(filename, 'w') as file:
      json.dump(products, file, indent=4)



def filter_by_category(products: List[Dict[str, Any]] , category: int) -> List[Dict[str, Any]] :
  """
  Xuất danh sách sản phẩm theo mục
  Args:
  products (List[Dict[str, Any]]) : Danh sách sản phẩm
  category (int) : Danh mục sản phẩm
  Return:
  List[Dict[str, Any]] : Danh sách sản phẩm theo mục
  """
  for product in products :
    if product["category"] == category :
      print(product)
  return products
if __name__ == '__main__':
    filename = "products.json"
    products = load_data(filename)

    category = "Electronics"
    products = filter_by_category(products, category)
    print(f"Danh sách sản phẩm trong danh mục {category}")