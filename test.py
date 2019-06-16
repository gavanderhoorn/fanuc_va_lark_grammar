#!/usr/bin/env python

# Copyright (c) 2019, G.A. vd. Hoorn
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author G.A. vd. Hoorn

# primitive test. TODO: use nose or somethimg

from os import path

from lark import Lark


file_loc = path.dirname(path.realpath(__file__))
tests_loc = path.join(file_loc, 'test_vas')
GRAMMAR=path.join(file_loc, 'grammar.lark')

parser = Lark(open(GRAMMAR), start='va_file')


with open(path.join(tests_loc, 'config_value.va'), 'r') as f:
    parser.parse(f.read())

with open(path.join(tests_loc, 'position_value.va'), 'r') as f:
    parser.parse(f.read())

with open(path.join(tests_loc, 'jointpos9_value.va'), 'r') as f:
    parser.parse(f.read())

with open(path.join(tests_loc, '2d_array_value.va'), 'r') as f:
    parser.parse(f.read())

with open(path.join(tests_loc, 'xyzwpr_value.va'), 'r') as f:
    parser.parse(f.read())

with open(path.join(tests_loc, 'primitives_struct_value.va'), 'r') as f:
    parser.parse(f.read())

with open(path.join(tests_loc, 'builtins_value.va'), 'r') as f:
    parser.parse(f.read())
