#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import pytest
from pythoncode.calculator import calculator


def get_datas():
    with open('./datas/calc.yml', encoding='utf-8')as f:
        testdata = yaml.safe_load(f)  # yaml数据读进来
        adddatas = testdata['add']['datas']
        addids = testdata['add']['ids']
        divdatas = testdata['div']['datas']
        divids = testdata['div']['ids']
        divdatafloats = testdata['div']['datafloats']
        dividfloats = testdata['div']['idfloats']
        adderrors = testdata['add']['err']
        diverrors = testdata['div']['err']
        # print([adddatas, addids])
        return [adddatas, addids, divdatas, divids, divdatafloats, dividfloats, adderrors, diverrors]


class TestCalc:

    def setup_class(self):
        self.calc = calculator()  # 定义一个实例变量，以替换每个方法中实例化步骤
        print("开始")

    def teardown_class(self):
        print("结束")

    def setup(self):  # 每个模块开始都会被调用，所以testa执行之前调用一次，testa2执行之前调用一次
        print("开始计算")

    def teardown(self):  # 每个模块开始都会被调用，所以testa执行之前调用一次，testa2执行之前调用一次
        print("结束计算")

    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    @pytest.mark.add
    def test_add(self, a, b, expect):
        # calc = calculator()   #实例化
        result = self.calc.add(a, b)
        assert expect == result

    # '''
    @pytest.mark.parametrize('a,b,expect', [
        (0.1, 0.2, 0.3),
        (0.1, 0.1, 0.2),
        (100.8761, 56.6544, 157.5305),
        (100.11111111, 100.11111111, 200.22222222),
        (-5.56, 10.31, 4.75)
    ])
    # '''
    def test_add_float(self, a, b, expect):
        # calc = calculator()   #实例化
        result = round(self.calc.add(a, b), 8)
        assert expect == result

    @pytest.mark.parametrize('a,b,expect', get_datas()[2], ids=get_datas()[3])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert expect == result

    @pytest.mark.parametrize('a,b,expect', get_datas()[4], ids=get_datas()[5])
    def test_div_float(self, a, b, expect):
        result = round(self.calc.div(a, b), 8)
        assert expect == result

    @pytest.mark.parametrize('a,b', get_datas()[6])
    def test_add_error(self, a, b):
        try:
            result_e3 = self.calc.add(a, b)
        except ValueError:
            print('error非数值')
        except TypeError:
            print('error类型错误')
        except:
            print('error')
        else:
            print('OK')

    @pytest.mark.parametrize('a,b', get_datas()[7])
    def test_div_error(self, a, b):
        try:
            result_e4 = self.calc.div(a, b)
        except ZeroDivisionError:
            print('error除数0')
        except ValueError:
            print('error非数值')
        except TypeError:
            print('error类型错误')
        except:
            print('error')
        else:
            print('OK')
