# -*- coding: utf-8 -*-

from module.plugins.internal.SimpleCrypter import SimpleCrypter, create_getInfo


class CrockoComFolder(SimpleCrypter):
    __name__    = "CrockoCom"
    __type__    = "crypter"
    __version__ = "0.03"
    __status__  = "testing"

    __pattern__ = r'http://(?:www\.)?crocko\.com/f/.+'
    __config__  = [("activated"         , "bool", "Activated"                          , True),
                   ("use_premium"       , "bool", "Use premium account if available"   , True),
                   ("use_subfolder"     , "bool", "Save package to subfolder"          , True),
                   ("subfolder_per_pack", "bool", "Create a subfolder for each package", True)]

    __description__ = """Crocko.com folder decrypter plugin"""
    __license__     = "GPLv3"
    __authors__     = [("zoidberg", "zoidberg@mujmail.cz")]


    LINK_PATTERN = r'<td class="last"><a href="(.+?)">download</a>'


getInfo = create_getInfo(CrockoComFolder)
