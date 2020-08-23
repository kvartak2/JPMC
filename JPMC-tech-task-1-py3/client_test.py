import unittest
from client3 import *

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_ChkRatio(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    prices = {}
    for quote in quotes:
      stock, bid_price, ask_price, price = quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2
      prices[stock] = price
    self.assertEqual(getRatio(prices['ABC'], prices['DEF']), (prices['ABC']/prices['DEF']))

  def test_getDataPoint_ChkDividedByZero(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0.0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    prices = {}
    for quote in quotes:
      stock, bid_price, ask_price, price = quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2
      prices[stock] = price
    self.assertEqual(getRatio(prices['ABC'], prices['DEF']), (None))
  """ ------------ Add more unit tests ------------ """

  def test_Price_a_zero(self):
    price_a = 0
    price_b = 111.1
    self.assertEqual(getRatio(price_a, price_b),0.0)

if __name__ == '__main__':
    unittest.main()
