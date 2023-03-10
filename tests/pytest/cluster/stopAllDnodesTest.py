###################################################################
#           Copyright (c) 2016 by TAOS Technologies, Inc.
#                     All rights reserved.
#
#  This file is proprietary and confidential to TAOS Technologies.
#  No part of this file may be reproduced, stored, transmitted,
#  disclosed or used in any form or by any means other than as
#  expressly provided by the written permission from Jianhui Tao
#
###################################################################

# -*- coding: utf-8 -*-

import sys
from clusterSetup import *
from util.sql import tdSql
from util.log import tdLog
import random

class ClusterTestcase:
    
    ## test case 19 ##
    def run(self):

        nodes = Nodes()
        ctest = ClusterTest(nodes.node1.hostName)
        tdSql.init(ctest.conn.cursor(), False)
                
        tdSql.query("select * from information_schema.ins_databases")
        count = tdSql.queryRows;

        nodes.stopAllTaosd()
        nodes.node1.startTaosd()
        tdSql.error("select * from information_schema.ins_databases")

        nodes.node2.startTaosd()
        tdSql.error("select * from information_schema.ins_databases")

        nodes.node3.startTaosd()
        tdLog.sleep(10)
        tdSql.query("select * from information_schema.ins_databases")
        tdSql.checkRows(count)

ct = ClusterTestcase()
ct.run()
