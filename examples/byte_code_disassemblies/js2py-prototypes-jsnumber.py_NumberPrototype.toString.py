60  class NumberPrototype:
61      def toString(radix):
62          if this.Class != 'Number':
63              raise this.MakeError('TypeError',
64                                   'Number.prototype.valueOf is not generic')
65          if radix.is_undefined():
66              return to_str_rep(this)
67          r = radix.to_int()
68          if r == 10:
69              return to_str_rep(this)
70          if r not in xrange(2, 37):
71              raise this.MakeError(
72                  'RangeError',
73                  'Number.prototype.toString() radix argument must be between 2 and 36'
74              )
75          num = this.to_int()
76          if num < 0:
77              num = -num
78              sign = '-'
79          else:
80              sign = ''
81          res = ''
82          while num:
83              s = RADIX_SYMBOLS[num % r]
84              num = num // r
85              res = s + res
86          return sign + (res if res else '0')
