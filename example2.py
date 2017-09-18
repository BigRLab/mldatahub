#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep

from mldatahub.config.config import global_config
from mldatahub.odm.dataset_dao import DatasetDAO

__author__ = "Iván de Paz Centeno"

session = global_config.get_session()
DatasetDAO.query.remove()

dataset = DatasetDAO("ip/asd4", "example4", "desc", "none")
ele = dataset.add_element("ele1", "description of the element.", 0, tags=["tag1", "tag2"])
session.flush()
session.refresh(dataset)
print(dataset.elements[0])

print(ele)
dataset.delete()
#session.flush()

print(dataset)