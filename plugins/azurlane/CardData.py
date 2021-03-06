# 轻型舰
import random


class NormalLightShipData:
    normalLightShip = ['卡辛', '唐斯', '克雷文', '麦考尔', '奥利克', '富特', '斯彭斯', '奥马哈', '罗利', '小猎兔犬', '大斗犬', '彗星', '新月', '小天鹅',
                       '狐提', '利安得', '长良', '柯尼斯堡', '卡尔斯鲁厄', '科隆', '睦月', '如月', '卯月']
    rareLightShip = ['弗莱彻', '撒切尔', '本森', '西姆斯', '哈曼', '布鲁克林', '菲尼克斯', '亚特兰大', '朱诺', '女将', '阿卡司塔', '热心', '命运女神', '天后',
                     '阿基里斯', '阿贾克斯', '初春', '初霜', '有名', '夕暮', '莱比锡', '贝利', '神风', '松风', '泽西', '浦风', '矶风‌', '谷风', '大潮',
                     '布什‌', '孟菲斯', '康克德', '牙买加', '库拉索', '杓鹬']
    eliteLightShip = ['莫里', '拉菲', '海伦娜', '克利夫兰', '标枪', '吸血鬼', '爱丁堡', '欧罗拉', '吹雪', '凌波', '野分', '夕张', 'Z23', '逸仙', '宁海',
                      '平海', '圣路易斯', '丹佛', '小贝法', '小克利夫兰', '小海伦娜', '谢菲尔德', '无敌', '追赶者']
    superRareLightShip = ['圣地亚哥', '贝尔法斯特', '明石', '蒙彼利埃', '雀捷', '天狼星']

    # 一样还是分区间算法吧. [1-10000]
    # 超稀有 7%  6搜 -> [1-700]
    # 精锐  12% 24搜 -> [701-1900]
    # 稀有  26% 35搜 -> [1901-4500]
    # 普通  55% 23搜 -> [4501-10000]
    def singleDrawing(self):
        randomResult = random.randint(1, 10000)
        if randomResult <= 700:
            # 超稀有
            return '★★★★★★【超稀有】' + self.superRareLightShip[random.randint(0, 5)]
        elif randomResult <= 1900:
            # 精锐
            return '★★★★★【精锐】' + self.eliteLightShip[random.randint(0, 23)]
        elif randomResult <= 4500:
            # 稀有
            return '☆☆☆☆☆[稀有]' + self.rareLightShip[random.randint(0, 34)]
        else:
            # 普通
            return '☆☆☆☆[普通]' + self.normalLightShip[random.randint(0, 22)]


class HeavyShipData:
    normalHeavyShip = ['彭萨科拉', '内华达', '俄克拉荷马', '青叶', '衣笠']
    rareHeavyShip = ['北安普顿', '芝加哥', '波特兰', '宾夕法尼亚', '田纳西', '加利福尼亚', '什罗普郡', '肯特‌', '萨福克', '诺福克', '反击', '伊势', '日向',
                     '苏塞克斯']
    eliteHeavyShip = ['休斯敦‌', '印第安纳波利斯', '威奇塔‌', '亚利桑那', '爱丁堡', '伦敦', '多塞特郡', '约克‌', '埃克塞特', '声望‌', '伊丽莎白女王', '纳尔逊',
                      '罗德尼', '黑暗界', '恐怖', '德意志', '斯佩伯爵海军上将', '阿贝克隆比']
    superRareHeavyShip = ['贝尔法斯特', '胡德', '厌战', '威尔士亲王', '高雄', '爱宕‌', '欧根亲王', '约克公爵']

    # 超稀有 7%  8搜 -> [1-700]
    # 精锐  12% 18搜 -> [701-1900]
    # 稀有  51% 14搜 -> [1901-7000]
    # 普通  30% 5搜 -> [7001-10000]
    def singleDrawing(self):
        randomResult = random.randint(1, 10000)
        if randomResult <= 700:
            # 超稀有
            return '★★★★★★【超稀有】' + self.superRareHeavyShip[random.randint(0, 7)]
        elif randomResult <= 1900:
            # 精锐
            return '★★★★★【精锐】' + self.eliteHeavyShip[random.randint(0, 17)]
        elif randomResult <= 4500:
            # 稀有
            return '☆☆☆☆☆[稀有]' + self.rareHeavyShip[random.randint(0, 13)]
        else:
            # 普通
            return '☆☆☆☆[普通]' + self.normalHeavyShip[random.randint(0, 4)]


# 特型舰
class SpecialShipData:
    normalSpecialShip = ['彭萨科拉', '博格', '兰利', '突击者', '竞技神']
    rareSpecialShip = ['北安普顿', '芝加哥', '波特兰', '长岛', '什罗普郡', '肯特‌', '萨福克', '诺福克']
    eliteSpecialShip = ['休斯敦‌', '印第安纳波利斯', '威奇塔‌', '列克星敦', '萨拉托加', '约克城', '大黄蜂', '女灶神‌', '爱丁堡', '伦敦', '多塞特郡', '独角兽',
                        '皇家方舟', '光荣', '伊26', '伊58', '鲦鱼‌', '追赶者']
    superRareSpecialShip = ['企业', '贝尔法斯特', '光辉', '高雄‌', '爱宕', '‌翔鹤‌', '瑞鹤‌', '明石‌', '欧根亲王', '伊19‌', 'U81', '半人马', '胜利']

    # 超稀有 7%  13搜 -> [1-700]
    # 精锐  12% 18搜 -> [701-1900]
    # 稀有  51% 8搜 -> [1901-7000]
    # 普通  30% 5搜 -> [7001-10000]
    def singleDrawing(self):
        randomResult = random.randint(1, 10000)
        if randomResult <= 700:
            # 超稀有
            return '★★★★★★【超稀有】' + self.superRareSpecialShip[random.randint(0, 12)]
        elif randomResult <= 1900:
            # 精锐
            return '★★★★★【精锐】' + self.eliteSpecialShip[random.randint(0, 17)]
        elif randomResult <= 4500:
            # 稀有
            return '☆☆☆☆☆[稀有]' + self.rareSpecialShip[random.randint(0, 7)]
        else:
            # 普通
            return '☆☆☆☆[普通]' + self.normalSpecialShip[random.randint(0, 4)]


# 限时建造
class MNFLeMalinSpecialData:
    # 特殊概率：恶毒2% 让巴尔，马萨诸塞1.8%
    mNFLeMalinSpecialOnepointEight = ['让·巴尔', '马萨诸塞']
    mNFLeMalinSpecialTwoPointFive = ['倔强‌', '敦刻尔克‌', '絮库夫']

    # 超稀有 7%  -> [1-700]
    # 精锐  12%  -> [701-1900]
    # 稀有  51%  -> [1901-7000]
    # 普通  30%  -> [7001-10000]
    # 特殊 11.3% -> [1-1130]
    def singleDrawing(self):
        randomResult = random.randint(1, 10000)
        if randomResult <= 1130:
            # 特殊建造
            randomResult = random.randint(1, 11300)
            # 恶毒                2%   -> [1,2000]
            # 让·巴尔 马萨诸塞     1.8% -> [2001,3800]
            # 倔强,敦刻尔克,絮库夫 2.5% -> [3801, 6300]
            # 福尔班              5%   -> [6301，11300]
            if randomResult <= 2000:
                return '★★★★★★【超稀有UP!】恶毒'
            elif randomResult <= 3800:
                return '★★★★★★【超稀有UP!】' + self.mNFLeMalinSpecialOnepointEight[random.randint(0, 1)]
            elif randomResult <= 6300:
                return '★★★★★【精锐UP!】' + self.mNFLeMalinSpecialTwoPointFive[random.randint(0, 2)]
            elif randomResult <= 11300:
                return '☆☆☆☆☆[稀有UP!]福尔班'
        else:
            # 普通建造
            randomResult = random.randint(1, 10000)
            if randomResult <= 700:
                # 超稀有
                return '★★★★★★【超稀有】非限时船'
            elif randomResult <= 1900:
                # 精锐
                return '★★★★★【精锐】非限时船'
            elif randomResult <= 4500:
                # 稀有
                return '☆☆☆☆☆[稀有]非限时船'
            else:
                # 普通
                return '☆☆☆☆[普通]非限时船'
