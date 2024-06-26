#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2023 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# All constants

# constants for configs
GLOBAL = "global"
LOCAL = "local"
DEFAULT_WHITE_LIST = "*"
EMPTY_WHITE_LIST = None

# config name
BASE_CONFIG = "base_config"
COMPOSABLE_CONFIG = "composable_config"
RTN_WEIGHT_ONLY_QUANT = "rtn_weight_only_quant"
STATIC_QUANT = "static_quant"
GPTQ = "gptq"


from typing import Callable, Union

OP_NAME_OR_MODULE_TYPE = Union[str, Callable]
