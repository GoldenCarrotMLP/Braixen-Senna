#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Senna/Senna.bin"
    "DATA/Senna_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin32_Skins_Skin33_Skins_Skin34_Skins_Skin35_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Characters/Senna/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/Senna/Skins/Root" = SkinCharacterDataProperties {
        skinClassification: u32 = 1
        championSkinName: string = "Senna"
        metaDataTags: string = "faction:shadowisles,gender:female,race:human"
        skinAudioProperties: embed = skinAudioProperties {
            tagEventList: list[string] = {
                "Senna"
            }
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "Senna_Base_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Senna/Skins/Base/Senna_Base_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Senna/Skins/Base/Senna_Base_SFX_events.bnk"
                    }
                }
                BankUnit {
                    name: string = "Senna_Base_VO"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Senna/Skins/Base/Senna_Base_VO_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Senna/Skins/Base/Senna_Base_VO_events.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Senna/Skins/Base/Senna_Base_VO_audio.wpk"
                    }
                    events: list[string] = {
                        "Play_vo_Senna_Attack2DGeneral"
                        "Play_vo_Senna_Dance3DGeneral"
                        "Play_vo_Senna_Death3D"
                        "Play_vo_Senna_FirstEncounter3DDemacia"
                        "Play_vo_Senna_FirstEncounter3DElise"
                        "Play_vo_Senna_FirstEncounter3DFiddlesticks"
                        "Play_vo_Senna_FirstEncounter3DGeneral"
                        "Play_vo_Senna_FirstEncounter3DHecarim"
                        "Play_vo_Senna_FirstEncounter3DKaisa"
                        "Play_vo_Senna_FirstEncounter3DLucian"
                        "Play_vo_Senna_FirstEncounter3DLunari"
                        "Play_vo_Senna_FirstEncounter3DLux"
                        "Play_vo_Senna_FirstEncounter3DMaokai"
                        "Play_vo_Senna_FirstEncounter3DMorgana"
                        "Play_vo_Senna_FirstEncounter3DNocturne"
                        "Play_vo_Senna_FirstEncounter3DShadowIsles"
                        "Play_vo_Senna_FirstEncounter3DSylas"
                        "Play_vo_Senna_FirstEncounter3DThresh"
                        "Play_vo_Senna_FirstEncounter3DVayne"
                        "Play_vo_Senna_FirstEncounter3DYorick"
                        "Play_vo_Senna_FirstEncounter3DYuumi"
                        "Play_vo_Senna_FirstMove2DWithLucianNear"
                        "Play_vo_Senna_Joke3DFeatherknight"
                        "Play_vo_Senna_Kill3DGeneral"
                        "Play_vo_Senna_Kill3DLucian"
                        "Play_vo_Senna_Kill3DShadowIsles"
                        "Play_vo_Senna_Kill3DThresh"
                        "Play_vo_Senna_Laugh3DGeneral"
                        "Play_vo_Senna_Move2DFirst"
                        "Play_vo_Senna_Move2DLong"
                        "Play_vo_Senna_Move2DStandard"
                        "Play_vo_Senna_Recall3DGeneral"
                        "Play_vo_Senna_Respawn2DGeneral"
                        "Play_vo_Senna_SennaBasicAttackSouls_cast3D"
                        "Play_vo_Senna_SennaE_cast3D"
                        "Play_vo_Senna_SennaQ_cast3D"
                        "Play_vo_Senna_SennaQ_cast3DLucian"
                        "Play_vo_Senna_SennaR_cast3D"
                        "Play_vo_Senna_SennaW_cast3D"
                        "Play_vo_Senna_Taunt3DGeneral"
                        "Play_vo_Senna_TauntResponse3DGeneral"
                        "Play_vo_Senna_WithLucianNear_FirstEncounter3D01Thresh_Chat02"
                        "Play_vo_Senna_WithLucianNear_FirstMove2D01_Chat02"
                        "Play_vo_Senna_WithLucianNear_FirstMove2D01_Chat04"
                        "Play_vo_Senna_WithLucianNear_FirstMove2D02_Chat03"
                        "Play_vo_Senna_WithLucianNear_FirstMove2D03_Chat03"
                        "Play_vo_Senna_WithLucianNear_FirstMove2D04_Chat02"
                        "Play_vo_Senna_WithLucianNear_FirstMove2D05_Chat02"
                        "Play_vo_Senna_WithLucianNear_FirstMove2D07_Chat03"
                        "Play_vo_Senna_WithLucianNear_FirstMove2D08_Chat02"
                        "Play_vo_Senna_WithLucianNear_Heal2D"
                        "Play_vo_Senna_WithLucianNear_Heal2D02_Chat02"
                        "Play_vo_Senna_WithLucianNear_KillChampion3D01_Chat02"
                        "Play_vo_Senna_WithLucianNear_KillChampion3D02_Chat02"
                        "Play_vo_Senna_WithLucianNear_KillChampion3D03_Chat02"
                    }
                    voiceOver: bool = true
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/Senna/Animations/Skin0"
        }
        armorMaterial: string = "Flesh"
        defaultAnimations: list[string] = {
            "Buffbones"
            "Buffbone_Additive"
        }
        iconAvatar: string = "ASSETS/Characters/Senna/HUD/Senna_Circle_0.dds"
        mContextualActionData: link = "Characters/Senna/CAC/Senna_Base"
        iconCircle: option[string] = {
            "ASSETS/Characters/Senna/HUD/Senna_Circle_0.dds"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/Senna/HUD/Senna_Square.dds"
        }
    }
}
