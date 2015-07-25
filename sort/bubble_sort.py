# py-sorting <http://github.com/GrowingWithTheWeb/py-sorting>
# Copyright 2015 Daniel Imms <http://www.growingwiththeweb.com>
# Released under the MIT license <http://github.com/GrowingWithTheWeb/py-sorting/blob/master/LICENSE>

import common.helpers as helpers

def sort(list, compare=helpers.compare):
  for i in range(0, len(list) - 1):
    for j in range(1, len(list) - i):
      if compare(list[j - 1], list[j]) > 0:
        helpers.swap(list, j, j - 1);
  return list
